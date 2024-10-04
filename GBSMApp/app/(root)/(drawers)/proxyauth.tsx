import { Redirect } from "expo-router";
import {
  StyleSheet,
} from "react-native";

const ProxyLogin = () => {
   return <Redirect href="/(auth)/welcome" />;

};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
export default ProxyLogin;
