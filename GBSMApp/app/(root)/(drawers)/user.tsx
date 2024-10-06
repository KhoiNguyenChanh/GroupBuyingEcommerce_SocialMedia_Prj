import { Text, View, StyleSheet, TouchableOpacity } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';

const UserScreen= () => {
 const { id } = useLocalSearchParams();
  const route = useRouter();
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Hồ Sơ Người Dùng</Text>
      <Text style={styles.content}>ID Người Dùng: {id}</Text>
      <TouchableOpacity
      onPress={ () => route.push("/otherscreens\\userinfoedit")}>
        <Text>Chỉnh sửa thông tin người dùng</Text>
      </TouchableOpacity>
    </View>
  );
}

export default UserScreen;
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    justifyContent: 'center',
  },
  title: {
    fontSize: 22,
    marginBottom: 12,
    textAlign: 'center',
  },
  content: {
    fontSize: 16,
    textAlign: 'center',
  },
});

