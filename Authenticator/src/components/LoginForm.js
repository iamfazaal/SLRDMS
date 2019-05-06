import React, { Component } from 'react';
import { View, Button, Text, ActivityIndicator } from 'react-native';
import { Keyboard, TouchableWithoutFeedback, TextInput } from 'react-native';
import Input from './Input';
import firebase from 'firebase';
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

    onLoginSuccess() {
        this.setState({
            email: '', password: '', error: '', loading: false
        })
    }

    onLoginFailure(errorMessage) {
        this.setState({ error: errorMessage, loading: false })
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
                    title="Sign in"
                    onPress={this.onButtonPress.bind(this)}
                />
                                    <Button
                    title="Sign up"
                    onPress={this.onButtonPress.bind(this)}
                />
                </View>
                // <Button
                //     title="Sign in"
                //     onPress={this.onButtonPress.bind(this)}
                // />,
                //  <Button
                //      title="Sign Up"
                //      onPress={this.onButtonPress.bind(this)}
                // />
            )
    
            }
    }

    render() {
        return (
            <View>
                <Input label="Email"
                    placeholder="user@mail.com"
                    value={this.state.email}
                    secureTextEntry={false}
                    keyboardType = 'email-address'
                    onChangeText={email => this.setState({ email })}
                />
                <Input label="Password"
                    placeholder="password"
                    value={this.state.password}
                    secureTextEntry={true}
                    onChangeText={password => this.setState({ password })}
                />

                {this.renderButton()}

                <Text style={styles.errorTextStyle}>
                    {this.state.error}
                </Text>
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
const styles = {
    errorTextStyle: {
        fontSize: 18,
        alignSelf: 'center',
        color: 'red'
    },
    spinnerStyle: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
      }
}

