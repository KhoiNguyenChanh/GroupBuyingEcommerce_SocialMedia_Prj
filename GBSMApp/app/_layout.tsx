import {
  DarkTheme,
  DefaultTheme,
  ThemeProvider,
} from "@react-navigation/native";
import { useFonts } from "expo-font";
import { Stack, useRouter } from "expo-router";
import * as SplashScreen from "expo-splash-screen";
import { useEffect, useReducer } from "react";
import "react-native-reanimated";

import { useColorScheme } from "@/hooks/useColorScheme";
import MyContext from "@/lib/MyContext";
import MyUserReducer from "@/lib/MyUserReducer";

// Prevent the splash screen from auto-hiding before asset loading is complete.
SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  // const colorScheme = useColorScheme();
  const [loaded] = useFonts({
    SpaceMono: require("../assets/fonts/SpaceMono-Regular.ttf"),
  });

  useEffect(() => {
    if (loaded) {
      SplashScreen.hideAsync();
    }
  }, [loaded]);

  const router = useRouter();
  // useeffect de so sanh viec user dang nhap xong se toi giao dien nào
  useEffect(() => {
    if (user) {
      router.replace("/(drawers)/(tabs)/main")
    }else {
      router.replace("/(auth)/welcome")
    }
  })
  // if (!loaded) {
  //   return null;
  // }
  const [user, dispatch] = useReducer(MyUserReducer,null);

  return (
    <MyContext.Provider value={[user, dispatch]}>
      <Stack>
        <Stack.Screen name="index" options={{ headerShown: false }} />
       
       
        <Stack.Screen name="(auth)" options={{ headerShown: false }} />
        <Stack.Screen name="(root)" options={{ headerShown: false }} />
        <Stack.Screen name="otherscreens" options={{ headerShown: false }} />

        <Stack.Screen name="+not-found" />
      </Stack>
    </MyContext.Provider>
  );
}
