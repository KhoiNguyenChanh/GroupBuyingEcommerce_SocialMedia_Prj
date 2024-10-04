import { Image, StyleSheet, Platform, View, Text } from 'react-native';

const UserScreen= () => {
  return (
    <View>
        <Text>
            UserScrean
        </Text>
    </View>
  );
}

export default UserScreen;
const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
