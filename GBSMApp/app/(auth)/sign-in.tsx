// import { Image, StyleSheet, Platform, View, Text, TouchableOpacity, } from 'react-native';
// import { SafeAreaView } from 'react-native-safe-area-context';
// import { useRouter } from 'expo-router';
// const SignInScreen = () => {
//     const router = useRouter();
//   return (
//     <SafeAreaView>
//         <Text style={styles.title}>Đăng nhập</Text>
//       {/* Thêm các trường nhập liệu cho đăng nhập tại đây */}

//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => router.back()} // Quay lại màn hình trước
//       >
//         <Text style={styles.buttonText}>Quay lại</Text>
//       </TouchableOpacity>
//     </SafeAreaView>

//   );
// }
// export default SignInScreen;

// const styles = StyleSheet.create({
//     container: {
//       flex: 1,
//       padding: 20,
//       backgroundColor: '#fff',
//       justifyContent: 'center',
//       alignItems: 'center',
//     },
//     title: {
//       fontSize: 28,
//       fontWeight: '600',
//       marginBottom: 20,
//     },
//     button: {
//       backgroundColor: '#2196F3',
//       paddingVertical: 12,
//       paddingHorizontal: 40,
//       borderRadius: 8,
//       marginTop: 30,
//     },
//     buttonText: {
//       color: '#fff',
//       fontSize: 18,
//       fontWeight: '500',
//     },
//   });

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
import Ionicons from "react-native-vector-icons/Ionicons";
import { SafeAreaView } from "react-native-safe-area-context";
import { useRouter } from "expo-router";
import { useState } from "react";
const SignInScreen = () => {
  const route = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleLogin = () => {
    route.push("/(root)/(drawers)/(tabs)/main");
    // Xử lý đăng ký ở đây
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Confirm Password:", confirmPassword);
  };
  const handleNavigateSignup = () => {
    route.push("/(auth)/sign-up");
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

          <Text style={styles.title}>Đăng nhập vào tài khoản</Text>
        </View>
        <View style={styles.InputContainer}>
          <Text style={{ width: "100%", marginBottom: 5 }}>
            Hãy nhập các thông tin yêu cầu{" "}
          </Text>

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
          <TouchableOpacity onPress={handleLogin} style={styles.button}>
            <Text style={styles.buttonText}>Đăng nhập</Text>
          </TouchableOpacity>
        </View>
        <View style={{ justifyContent: "center", alignItems: "center" }}>
          {/* lam sao de co dong gach ngang qua chu hoac? */}
          <Text style={{marginBottom:10,}}>Hoặc</Text>

          <View style={{ flexDirection: "row" }}>
            <TouchableOpacity
              onPress={() => handleNavigateSignup()}
              style={{ 
                backgroundColor: "#fff7e6",
                borderRadius: 10,
                flexDirection: 'row',
                alignItems: 'center', // Căn giữa icon và text
                padding: 10,
               }}
            >
              <Ionicons name="logo-google" size={20} color="#ff9b07" />
              <Text
                style={{
                  color: "#ff9b07",
                  lineHeight: 20,
                  fontSize: 14,
                  marginLeft:20,
                }}
              >
                Đăng nhập bằng Google
              </Text>
            </TouchableOpacity>
          </View>
        </View>

        <View
          style={{
            flexDirection: "row",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Text style={{ lineHeight: 20, fontSize: 14, margin: 12 }}>
            Chưa có tài khoản?
          </Text>
          <TouchableOpacity onPress={() => handleNavigateSignup()}>
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
              Đăng ký
            </Text>
          </TouchableOpacity>
        </View>
        <View style={{ justifyContent: "center", alignItems: "center" }}>
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
export default SignInScreen;

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
