import { Stack } from "expo-router";

const AuthLayout = () => {
  return (
    <Stack >
      <Stack.Screen
        name="welcome"
        options={{
          headerShown: true,
          headerTitle: "",
          headerStyle: { backgroundColor: "white"},
          headerShadowVisible: false
        }}
      />
      <Stack.Screen name="sign-in" options={{ headerShown: false }} />
      <Stack.Screen name="sign-up" options={{ headerShown: false }} />
    </Stack>
  );
};
export default AuthLayout;
