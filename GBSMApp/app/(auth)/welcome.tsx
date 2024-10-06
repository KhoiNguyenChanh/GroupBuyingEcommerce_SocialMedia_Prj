import { useNavigation } from "@react-navigation/native";
import { useRouter } from "expo-router";
import {
  Image,
  StyleSheet,
  Text,
  TouchableOpacity,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
const WelcomeScreen = () => {
  const route = useRouter();
  const navigation = useNavigation();
  return (
    <SafeAreaView style={styles.container}>
      <Image
        source={{ uri: "https://res.cloudinary.com/dbqaequqv/image/upload/t_Banner 16:9/v1727689598/welcome_p8yfr9.jpg" }}
        style={styles.image}
        resizeMode="contain"
      />
      {/* tạo trường hợp lưu tai khoan dang nhap r, text chào mừng là chào bạn {user.username?} */}
      <Text style={styles.welcomeText}>Chào mừng bạn !</Text>
      <Text>Bạn đã có tài khoản rồi?</Text>
      <TouchableOpacity
        onPress={() => route.push("/(auth)/sign-in")}
        style={styles.button}
      >
        <Text style={styles.buttonText}>Đăng nhập</Text>
      </TouchableOpacity>
      <Text>Bạn chưa có tài khoản ?</Text>

      <TouchableOpacity
        onPress={() => route.push("/(auth)/sign-up")}
        style={[styles.button, {backgroundColor:'#d37e00', width:'50%'}]}
      >
        <Text style={[styles.buttonText, ]}>Đăng ký</Text>
      </TouchableOpacity>
    </SafeAreaView>
  );
};
export default WelcomeScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1, // equivalent to 'h-full'
    alignItems: "center", // equivalent to 'items-center'
    justifyContent: "center", // equivalent to 'justify-between'
    backgroundColor: "white", // equivalent to 'bg-white'
  },
  image: {
    width: 500,
    height: 190,
    marginBottom: 20,
  },
  welcomeText: {
    fontSize: 24,
    fontWeight: "600",
    textAlign: "center",
    marginBottom: 30,
    color: "#333",
  },
  button: {
    backgroundColor: "#ffa500",
    paddingVertical: 12,
    paddingHorizontal: 40,
    borderRadius: 8,
    marginVertical: 10,
    width: "80%",
    alignItems: "center",
  },
  buttonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "500",
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: "absolute",
  },
});
