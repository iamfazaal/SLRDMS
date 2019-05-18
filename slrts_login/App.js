import React from 'react';
import { StyleSheet, Text, View} from 'react-native';
import LoginForm from './src/components/LoginForm';
import firebase from 'firebase';
import { Button } from 'react-native-elements';
import styles from "./src/components/style";

export default class App extends React.Component {
  
  componentDidMount(){
    let config = {
      apiKey: "AIzaSyAhazpdPSkZV4BefXIlC5ILe9hdh9rCBTM",
      authDomain: "slrts-1f893.firebaseapp.com",
      databaseURL: "https://slrts-1f893.firebaseio.com",
      projectId: "slrts-1f893",
      storageBucket: "slrts-1f893.appspot.com",
      messagingSenderId: "365005186440"
    };
    firebase.initializeApp(config);
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.setState({ loggedIn: true })
      } else {
        this.setState({ loggedIn: false })
      }
    })
  }

  constructor(props) {
    super(props);
    this.state = { email: '', password: '', error: ''};
}

renderComponent() {
  if (this.state.loggedIn) {
    return (
      <View style={styles.loginScreenContainer}>
      <View style={styles.loginFormView}>
      <Text style={styles.logoText}>SLRTS</Text>
     <Button
      buttonStyle={styles.signoutButton}
      title="Sign out"
      onPress={() => firebase.auth().signOut()}
      />
      </View>
      </View>
    );
  } else {
    return (
      <LoginForm />
    );
  }
}
  render() {
    return (
      // <View styles = {styles.container}>
      <View>
        {/* <Text>Open up App.js to start working on your app!</Text> */}
        {/* <Header title='SLRTS' /> */}
         {this.renderComponent()}
        {/* <LoginForm /> */}
        {/* <Header /> */}
        {/* <LoginNew /> */}
      </View>
    );
  }
}

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
// });
