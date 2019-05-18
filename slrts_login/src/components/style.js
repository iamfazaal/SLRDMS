const React = require("react-native");

const { StyleSheet } = React;

export default {

containerView: {
  flex: 1,
},
loginScreenContainer: {
  flex: 1,
},
logoText: {
  fontSize: 40,
  fontWeight: "800",
  marginTop: 150,
  marginBottom: 30,
  textAlign: 'center',
},
loginFormView: {
  flex: 1
},
loginFormTextInput: {
  height: 43,
  fontSize: 14,
  borderRadius: 5,
  borderWidth: 1,
  borderColor: '#eaeaea',
  backgroundColor: '#fafafa',
  paddingLeft: 10,
  marginLeft: 15,
  marginRight: 15,
  marginTop: 5,
  marginBottom: 5,

},
loginButton: {
  backgroundColor: '#2F43D3',
  borderRadius: 5,
  height: 45,
  marginLeft: 30,
  marginRight: 30,
  
  marginTop: 20,
},
signupButton: {
    backgroundColor: '#52EB66',
    borderRadius: 5,
    height: 45,
    marginLeft: 30,
    marginRight: 30,
    
    marginTop: 70,
  },
signoutButton: {
    backgroundColor: '#ff0000',
    borderRadius: 5,
    height: 45,
    marginTop: 10,
  },
fbLoginButton: {
  height: 45,
  marginTop: 10,
  backgroundColor: 'transparent',
},
errorTextStyle: {
    marginTop: -5,
    fontSize: 18,
    alignSelf: 'center',
    color: 'red'
},
spinnerStyle: {
    marginTop: 10,
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
},
};