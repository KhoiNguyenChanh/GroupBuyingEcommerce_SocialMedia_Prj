import { Tabs } from 'expo-router';
import { Drawer } from 'expo-router/drawer';
import React from 'react';

import { TabBarIcon } from '@/components/navigation/TabBarIcon';
import { Colors } from '@/constants/Colors';
import { useColorScheme } from '@/hooks/useColorScheme';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { Text, View } from 'react-native';

const DrawerLayout = () => {

  return (
      <Drawer>
      <Drawer.Screen name="(tabs)" options={{ headerShown: false }} />
        <Drawer.Screen
            name="funny" // This is the name of the page and must match the url from root
            options={{
              drawerLabel: 'Home',
              title: 'overview',
            }}
          />
          <Drawer.Screen
            name="user" // This is the name of the page and must match the url from root
            options={{
              drawerLabel: 'User',
              title: 'overview',
            }}
          />
      </Drawer>
    
  );
}
export default DrawerLayout;
