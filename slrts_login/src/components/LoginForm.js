import React, { Component } from 'react';
import { ActivityIndicator } from 'react-native';
//import { Keyboard, TouchableWithoutFeedback, TextInput } from 'react-native';
import Input from './Input';
import firebase from 'firebase';
import styles from "./style";
import {Keyboard, Text, View, TextInput, TouchableWithoutFeedback, Alert, KeyboardAvoidingView} from 'react-native';
import { Button } from 'react-native-elements';
//import { styles } from './LoginPageStyle';

export default class LoginForm extends Component {
    //   state = {email:'', password:''};
    constructor(props) {
        super(props);
        this.state = { email: '', password: '', error: '' };
    }

    onButtonPress() {
        this.setState({ error: '', loading: true })
        const { email, password } = this.state;
        firebase.auth().signInWithEmailAndPassword(email, password)
            .then(this.onLoginSuccess.bind(this))
            .catch(() => {
                firebase.auth().createUserWithEmailAndPassword(email, password)
                    .then(this.onLoginSuccess.bind(this))
                    .catch((error) => {
                        let errorCode = error.code
                        let errorMessage = error.message;
                        if (errorCode == 'auth/weak-password') {
                            this.onLoginFailure.bind(this)('Weak password!')
                        } else {
                            this.onLoginFailure.bind(this)(errorMessage)
                        }
                    });
            });
    }

    onLoginPress(){
        this.setState({ error: '', loading: true })
        const { email, password } = this.state;
        firebase.auth().signInWithEmailAndPassword(email, password)
        .then(this.onLoginSuccess.bind(this))
        .catch((error) => {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            if (errorCode === 'auth/wrong-password') {
                this.onLoginFailure.bind(this)('Wrong password.');
            } else {
                this.onLoginFailure.bind(this)(errorMessage);
            }
            console.log(error);
          });
    }

    onLoginSuccess() {
        this.setState({
            email: '', password: '', error: '', loading: false
        })
    }

    onLoginFailure(errorMessage) {
        this.setState({ error: alert(errorMessage), loading: false })
    }

    renderButton() {
        if (this.state.loading) {
            return (
                <View style={styles.spinnerStyle}>
                    <ActivityIndicator size={"small"} />
                </View>
            )
        } else {
            return (
                <View>
                <Button
                    buttonStyle={styles.loginButton}
                    title="Sign in"
                    onPress={this.onLoginPress.bind(this)}
                />
                <Button
                    buttonStyle={styles.signupButton}
                    title="Sign up"
                    onPress={this.onButtonPress.bind(this)}
                />
                </View>
            )
    
            }
    }

    render() {
        return (
            <View style={styles.loginScreenContainer}>
            <View style={styles.loginFormView}>
            <Text style={styles.logoText}>SLRTS</Text>
            <TextInput 
                    placeholder="user@mail.com"
                    placeholderColor="#c4c3cb"
                    value={this.state.email}
                    secureTextEntry={false}
                    keyboardType = 'email-address'
                    onChangeText={email => this.setState({ email })}
                    style={styles.loginFormTextInput} 
                />
                <TextInput 
                    placeholder="password"
                    placeholderColor="#c4c3cb"
                    value={this.state.password}
                    secureTextEntry={true}
                    onChangeText={password => this.setState({ password })}
                    style={styles.loginFormTextInput} 
                />

                {this.renderButton()}

                <Text style={styles.errorTextStyle}>
                    {this.state.error}
                </Text>
                </View>
        </View>
            // <TouchableWithoutFeedback onPress={() => Keyboard.dismiss()}>
            //     <View style={styles.loginPage}>
            //         <Text>Username</Text>
            //         <TextInput 
            //             style={styles.textInput}
            //             autoCorrect={false}
            //         />
            //         <Text>Password</Text>
            //         <TextInput 
            //             style={styles.textInput}
            //             autoCorrect={false}
            //             secureTextEntry={true}
            //             returnKeyType='go'
            //         />
            //     </View>
            // </TouchableWithoutFeedback>
        )
    }
}
// const styles = {
//     errorTextStyle: {
//         fontSize: 18,
//         alignSelf: 'center',
//         color: 'red'
//     },
//     spinnerStyle: {
//         flex: 1,
//         justifyContent: 'center',
//         alignItems: 'center'
//       }
// }


