import React, { PureComponent } from 'react';
import { Body, Button, Card, CardItem, Container, Content, Icon, Text } from 'native-base';
import { ScrollView, View, StyleSheet, Picker, Alert, AsyncStorage } from "react-native";

class forecast_page extends PureComponent {

    state = {
        names: [
            {
                'Monday': {
                    'Matara': '6:05',
                    'Weligama': '06:18:06:19',
                    'Ahangama': '06:26:06:27',
                    'Galle': '06:45:06:55',
                    'Hikkaduwa': '07:09:07:10',
                    'Ambalangoda': '07:20:07:21',
                    'Kosgoda': '07:31:07:32',
                    'Aluthgama': '07:41:07:42',
                    'Kaluthara South': '07:56:07:58',
                    'Colombo Fort': '08:43:08:45',
                    'Maradana': '8:49'
                },
                'Tuesday': {
                    'Matara': '6:06',
                    'Weligama': '06:19:06:20',
                    'Ahangama': '06:27:06:28',
                    'Galle': '06:46:06:56',
                    'Hikkaduwa': '07:10:07:11',
                    'Ambalangoda': '07:21:07:22',
                    'Kosgoda': '07:32:07:33',
                    'Aluthgama': '07:42:07:43',
                    'Kaluthara South': '07:57:07:59',
                    'Colombo Fort': '08:44:08:46',
                    'Maradana': '8:50'
                },
                'Wednesday': {
                    'Matara': '6:04',
                    'Weligama': '06:17:06:18',
                    'Ahangama': '06:25:06:26',
                    'Galle': '06:44:06:54',
                    'Hikkaduwa': '07:08:07:09',
                    'Ambalangoda': '07:19:07:20',
                    'Kosgoda': '07:30:07:31',
                    'Aluthgama': '07:40:07:41',
                    'Kaluthara South': '07:55:07:57',
                    'Colombo Fort': '08:42:08:44',
                    'Maradana': '8:48'
                },
                'Thursday': {
                    'Matara': '6:07',
                    'Weligama': '06:20:06:21',
                    'Ahangama': '06:28:06:29',
                    'Galle': '06:47:06:57',
                    'Hikkaduwa': '07:11:07:12',
                    'Ambalangoda': '07:22:07:23',
                    'Kosgoda': '07:33:07:34',
                    'Aluthgama': '07:43:07:44',
                    'Kaluthara South': '07:58:08:00',
                    'Colombo Fort': '08:45:08:47',
                    'Maradana': '8:51'
                },
                'Friday': {
                    'Matara': '6:08',
                    'Weligama': '06:21:06:22',
                    'Ahangama': '06:29:06:30',
                    'Galle': '06:48:06:58',
                    'Hikkaduwa': '07:12:07:13',
                    'Ambalangoda': '07:23:07:24',
                    'Kosgoda': '07:34:07:35',
                    'Aluthgama': '07:44:07:45',
                    'Kaluthara South': '07:59:08:01',
                    'Colombo Fort': '08:46:08:48',
                    'Maradana': '8:52'
                },
                'Saturday': {
                    'Matara': '6:06',
                    'Weligama': '06:19:06:20',
                    'Ahangama': '06:27:06:28',
                    'Galle': '06:46:06:56',
                    'Hikkaduwa': '07:10:07:11',
                    'Ambalangoda': '07:21:07:22',
                    'Kosgoda': '07:32:07:33',
                    'Aluthgama': '07:42:07:43',
                    'Kaluthara South': '07:57:07:59',
                    'Colombo Fort': '08:44:08:46',
                    'Maradana': '8:50'
                },
                'Sunday': {
                    'Matara': '6:07',
                    'Weligama': '06:20:06:21',
                    'Ahangama': '06:28:06:29',
                    'Galle': '06:47:06:57',
                    'Hikkaduwa': '07:11:07:12',
                    'Ambalangoda': '07:22:07:23',
                    'Kosgoda': '07:33:07:34',
                    'Aluthgama': '07:43:07:44',
                    'Kaluthara South': '07:58:08:00',
                    'Colombo Fort': '08:45:08:47',
                    'Maradana': '8:51'
                }
            }
        ],
        subject: null,
        content: null,
    }

    render() {
        return (
            <ScrollView>
                <Card style={styles.mb}>
                    <CardItem header bordered>
                        <Text>Forecast - Ruhunu Kumari Train</Text>
                    </CardItem>
                    {
                        this.state.names.map((item, index) => (
                            <View key={item.id} style={styles.item}>
                                <CardItem>
                                    <Body>
                                        <Text>{item.Monday}</Text>
                                        <Text numberOfLines={1} note>
                                            {item.dest}
                                        </Text>
                                    </Body>
                                </CardItem>
                            </View>
                        ))
                    }
                </Card>
            </ScrollView>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: "#FFF",
        flex: 1
    },
    mb: {
        marginBottom: 3,
        flex: 1
    },
    mb15: {
        marginBottom: 20
    },
    iconStyle: {
        color: '#0A69FE'
    },
    inputText: {
        height: 40,
        borderRadius: 1,
        borderWidth: 2,
        borderColor: '#686868',
    }

});

export default forecast_page;