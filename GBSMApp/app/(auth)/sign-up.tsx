import {
  Image,
  StyleSheet,
  Platform,
  View,
  Text,
  TouchableOpacity,
  ScrollView,
  TextInput,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import Ionicons from "react-native-vector-icons/Ionicons";

import { useRouter } from "expo-router";
import { useState } from "react";
const SignUpScreen = () => {
  const route = useRouter();
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [avatar, setAvatar] = useState(""); // Nếu cần nhập URL hoặc xử lý ảnh

  const handleNavigateLogin = () => {
    route.push("/(auth)/sign-in");
  };
  const handleRegister = () => {
    // Xử lý đăng ký ở đây
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Confirm Password:", confirmPassword);
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.subcontainer}>
        <View style={styles.imagecontainer}>
          <Image
            source={{
              uri: "https://res.cloudinary.com/dbqaequqv/image/upload/t_Banner 16:9/v1727713795/ecommerce_thgpkf.jpg",
            }}
            style={styles.image}
          />

          <Text style={styles.title}>Tạo tài khoản mới</Text>
        </View>
        <View style={styles.InputContainer}>
          <Text style={{ width: "100%", marginBottom: 5 }}>
            Hãy nhập các thông tin yêu cầu{" "}
          </Text>
          <TextInput
            style={styles.input}
            placeholder="Họ và tên lót"
            value={firstname}
            onChangeText={setFirstname}
          />
          <TextInput
            style={styles.input}
            placeholder="Tên"
            value={lastname}
            onChangeText={setLastname}
          />
          <TextInput
            style={styles.input}
            placeholder="Tên người dùng"
            value={username}
            onChangeText={setUsername}
          />
          <TextInput
            style={styles.input}
            placeholder="Email"
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
            autoCapitalize="none"
          />
          <TextInput
            style={styles.input}
            placeholder="Mật khẩu"
            value={password}
            onChangeText={setPassword}
            secureTextEntry
          />
          <TextInput
            style={styles.input}
            placeholder="Xác nhận mật khẩu"
            value={confirmPassword}
            onChangeText={setConfirmPassword}
            secureTextEntry
          />
          {/* <Text>Nhập ảnh, dùng button để lưu ảnh somehow :1 </Text> */}
          <TouchableOpacity onPress={handleRegister} style={styles.button}>
            <Text style={styles.buttonText}>Đăng ký</Text>
          </TouchableOpacity>
        </View>
        {/* dang ky bang Google */}
        <View style={{ justifyContent: "center", alignItems: "center" }}>
          {/* lam sao de co dong gach ngang qua chu hoac? */}
          <Text style={{ marginBottom: 10 }}>Hoặc</Text>

          <View style={{ flexDirection: "row" }}>
            <TouchableOpacity
              // onPress={() => handleSignup()}
              style={{
                backgroundColor: "#fff7e6",
                borderRadius: 10,
                flexDirection: "row",
                alignItems: "center", // Căn giữa icon và text
                padding: 10,
              }}
            >
              <Ionicons name="logo-google" size={20} color="#ff9b07" />
              <Text
                style={{
                  color: "#ff9b07",
                  lineHeight: 20,
                  fontSize: 14,
                  marginLeft: 20,
                }}
              >
                Đăng ký bằng Google
              </Text>
            </TouchableOpacity>
          </View>
          <View
            style={{
              flexDirection: "row",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <Text style={{ lineHeight: 20, fontSize: 14, margin: 12 }}>
              Đã có tài khoản?
            </Text>
            <TouchableOpacity onPress={() => handleNavigateLogin()}>
              <Text
                style={[
                  styles.underline,
                  {
                    color: "#ff9b07",
                    lineHeight: 20,
                    fontSize: 14,
                  },
                ]}
              >
                Đăng nhập
              </Text>
            </TouchableOpacity>
          </View>
        </View>

        <View
          style={{ justifyContent: "center", alignItems: "center", bottom: 20 }}
        >
          <TouchableOpacity
            style={[styles.button]}
            onPress={() => route.back()}
          >
            <Text style={styles.buttonText}>Quay lại</Text>
          </TouchableOpacity>
        </View>
      </View>
    </ScrollView>
  );
};
export default SignUpScreen;

const styles = StyleSheet.create({
  underline: {
    textDecorationLine: "underline",
  },
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  subcontainer: {
    flex: 1,
    backgroundColor: "#fff",
  },
  imagecontainer: {
    position: "relative",
    width: "100%",
    height: 250,
  },
  image: {
    zIndex: 0,
    width: "100%",
    height: 250,
    opacity: 0.75,
  },
  title: {
    fontSize: 24,
    color: "black",
    fontWeight: "600",
    bottom: 10,
    left: 20,
    position: "absolute",
  },
  button: {
    width: "70%",
    backgroundColor: "#ffa500",
    paddingVertical: 12,
    paddingHorizontal: 40,
    borderRadius: 8,
    marginTop: 20,
    alignItems: "center",
  },
  buttonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "500",
  },
  input: {
    height: 50,
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 8,
    paddingHorizontal: 10,
    marginBottom: 15,
    width: "100%",
  },
  InputContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 16,
    backgroundColor: "#fff",
  },
});
