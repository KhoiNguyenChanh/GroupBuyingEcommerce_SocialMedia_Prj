import { Redirect } from "expo-router";
import {
   
  StyleSheet,
  Text,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

const Chat = () => {
   return (
    <SafeAreaView>
        <Text>
            Chat
        </Text>
    </SafeAreaView>
   )
};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
export default Chat;
