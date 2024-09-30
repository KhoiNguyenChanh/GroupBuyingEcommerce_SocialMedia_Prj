import { Redirect } from "expo-router";
import {
  StyleSheet,
} from "react-native";

const Home = () => {
  return <Redirect href="/welcome" />;
};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
export default Home;
