import { Stack } from 'expo-router';
import {Drawer } from 'expo-router/drawer'
const Layout = () => {
  return (
      <Stack>
        <Stack.Screen name="(drawer)" options={{ headerShown: false }} />
        <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
        
      </Stack>
    //   <Drawer>
    //   <Drawer.Screen name="(tabs)" options={{ headerShown: false }} />
    //   <Drawer.Screen name="(drawer)" />
    // </Drawer>
  );
}

export default Layout;