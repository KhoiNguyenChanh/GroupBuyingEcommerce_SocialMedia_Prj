import MyContext from "@/lib/MyContext";
import { Stack } from "expo-router";
import { useContext } from "react";

const AuthLayout = () => {
  return (
    <Stack>
      <Stack.Screen
        name="welcome"
        options={{
          headerShown: true,
          headerTitle: "",
          headerStyle: { backgroundColor: "white" },
          headerShadowVisible: false,
        }}
      />
      <Stack.Screen name="sign-in" options={{ headerShown: false }} />

      <Stack.Screen name="sign-up" options={{ headerShown: false }} />
      <Stack.Screen name="sign-out" options={{ headerShown: false }} />
    
    </Stack>
  );
};
export default AuthLayout;
