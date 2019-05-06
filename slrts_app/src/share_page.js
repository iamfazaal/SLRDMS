import React, { PureComponent } from 'react';
import { Body, Button, Card, CardItem, Container, Content, Icon, Text } from 'native-base';
import { ScrollView, View, StyleSheet, Picker, Alert, AsyncStorage } from "react-native";

const uniqueId = require('react-native-unique-id')
import BackgroundGeolocation from "react-native-mauron85-background-geolocation";

class share_page extends PureComponent {

    hello = {
        id: 0,
    }

    state = { train: '' }
    updateTrain = (train) => {
        this.setState({ train: train })
    }

    constructor(props) {
        super(props);
        uniqueId((error, id) => {
            if (error) {
                return console.error(error);
            } else {
                this.hello.id = id;
            }
        });

        AsyncStorage.getItem('state', (err, result) => {
            if (result == 'run') {
                this.setState({ isRunning: false });
            } else {
                this.setState({ isRunning: true });
            }
        });
    }

    componentDidMount() {
        BackgroundGeolocation.configure({
            desiredAccuracy: 5,
            stationaryRadius: 5,
            distanceFilter: 8,
            notificationTitle: 'Sri Lanka Railway Tracking Simulator.',
            notificationText: 'Location Sharing.!',
            debug: true,
            startOnBoot: false,
            stopOnTerminate: false,
            locationProvider: BackgroundGeolocation.ACTIVITY_PROVIDER,
            interval: 1000,
            fastestInterval: 5000,
            activitiesInterval: 1000,
            stopOnStillActivity: false,
            url: 'http://192.168.1.7:3000/location',
            httpHeaders: {
                'Content-Type': 'application/json'
            },
            postTemplate: [this.hello.id, '@latitude', '@longitude', '@speed', this.state.train],
            syncThreshold: 100

        });

        //postTemplate: [this.state.uniqueID , '@latitude', '@longitude', '@speed', '@time', '@accuracy', '@bearing'],

        BackgroundGeolocation.on('location', (location) => {
            BackgroundGeolocation.startTask(taskKey => {
                BackgroundGeolocation.endTask(taskKey);
            });
        });

        BackgroundGeolocation.on('stationary', (stationaryLocation) => {
            Actions.sendLocation(stationaryLocation);
        });

        BackgroundGeolocation.on('error', (error) => {
            console.log('[ERROR] BackgroundGeolocation error:', error);
        });

        BackgroundGeolocation.on('start', () => {
            console.log('[DEBUG] BackgroundGeolocation has been started');
            this.setState({ isRunning: true });
        });

        BackgroundGeolocation.on('stop', () => {
            console.log('[DEBUG] BackgroundGeolocation has been stopped');
            this.setState({ isRunning: false });
        });

        BackgroundGeolocation.on('authorization', (status) => {
            console.log('[INFO] BackgroundGeolocation authorization status: ' + status);
            if (status !== BackgroundGeolocation.AUTHORIZED) {
                setTimeout(() =>
                    Alert.alert('App requires location tracking permission', 'Would you like to open app settings?', [
                        { text: 'Yes', onPress: () => BackgroundGeolocation.showAppSettings() },
                        { text: 'No', onPress: () => console.log('No Pressed'), style: 'cancel' }
                    ]), 1000);
            }
        });

        BackgroundGeolocation.on('background', () => {
            console.log('[INFO] App is in background');
        });

        BackgroundGeolocation.on('foreground', () => {
            console.log('[INFO] App is in foreground');
        });

        BackgroundGeolocation.on('abort_requested', () => {
            console.log('[INFO] Server responded with 285 Updates Not Required');
        });

        BackgroundGeolocation.on('http_authorization', () => {
            console.log('[INFO] App needs to authorize the http requests');
        });

        BackgroundGeolocation.checkStatus(status => {
            console.log('[INFO] BackgroundGeolocation service is running', status.isRunning);
            console.log('[INFO] BackgroundGeolocation services enabled', status.locationServicesEnabled);
            console.log('[INFO] BackgroundGeolocation auth status: ' + status.authorization);
        });
    }

    componentWillUnmount() {
        BackgroundGeolocation.removeAllListeners();
    }

    toggleTracking() {
        BackgroundGeolocation.checkStatus(({ isRunning, locationServicesEnabled, authorization }) => {
            if (isRunning) {
                AsyncStorage.setItem('state', 'stop');
                AsyncStorage.setItem('train', 'zero');
                BackgroundGeolocation.stop();
                return false;
            }

            if (!locationServicesEnabled) {
                Alert.alert(
                    'Location services disabled',
                    'Would you like to open location settings?',
                    [
                        {
                            text: 'Yes',
                            onPress: () => BackgroundGeolocation.showLocationSettings()
                        },
                        {
                            text: 'No',
                            onPress: () => console.log('No Pressed'),
                            style: 'cancel'
                        }
                    ]
                );
                return false;
            }

            if (authorization == 99) {
                AsyncStorage.setItem('state', 'run');
                BackgroundGeolocation.start();
            } else if (authorization == BackgroundGeolocation.AUTHORIZED) {
                AsyncStorage.setItem('state', 'run');

                BackgroundGeolocation.start();
            } else {
                Alert.alert(
                    'App requires location tracking',
                    'Please grant permission',
                    [
                        {
                            text: 'Ok',
                            onPress: () => BackgroundGeolocation.start(),
                            onPress: () => AsyncStorage.setItem('state', 'run'),
                        }
                    ]
                );
            }
        });
    }

    render() {
        return (
            <ScrollView>
                <Card style={styles.mb}>
                    <CardItem header bordered>
                        <Text>Sri Lanka Railway Tracking System.</Text>
                    </CardItem>
                    <CardItem>
                        <Body>
                            <Text>If you in train. you like to share you'r location for others.</Text>
                            <Text>Click ShareIT. After Select you'r train and click Share.</Text>
                            <Text>Before you check you'r app settings. Because its use for share location
                            process.</Text>
                            <Text></Text>
                        </Body>
                    </CardItem>
                </Card>
                <Card style={styles.mb}>
                    <CardItem header bordered>
                        <Text>Share Location</Text>
                    </CardItem>
                    <CardItem>
                        <Body>
                            <Picker
                                placeholder="Select you'r name of train"
                                selectedValue={this.state.train}
                                style={{ height: 50, width: 350 }}
                                onValueChange = {this.updateTrain}
                                enabled={this.state.isRunning}
                            >
                                <Picker.Item label="Ruhunu Kumari - Matara to Maradana" value="rk100" />
                                <Picker.Item label="Sagarika - Matara to Maradana" value="sg100" />
                                <Picker.Item label="Galu Kumari - Matara to Maradana" value="gk100" />
                                <Picker.Item label="Train no 01" value="tr100" />
                                <Picker.Item label="Train no 02" value="tr100" />
                            </Picker>

                            <Button block success onPress={this.toggleTracking}>
                                <Icon name={this.state.isRunning ? 'play' : 'pause'} style={styles.icon} />
                                <Text>Share Location</Text>
                            </Button>
                        </Body>
                    </CardItem>
                </Card>

            </ScrollView>
        );
    }
}

export default share_page;

const styles = StyleSheet.create({
    item: {
        flex: 1,
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: 30,
        margin: 2,
        borderColor: '#2a4944',
        borderWidth: 1,
        backgroundColor: '#d2f7f1'
    },
    mb: {
        marginBottom: 3,
        flex: 1
    },
    mb15: {
        marginBottom: 20
    },
    icon: {
        color: '#fff',
        fontSize: 30
    },
})