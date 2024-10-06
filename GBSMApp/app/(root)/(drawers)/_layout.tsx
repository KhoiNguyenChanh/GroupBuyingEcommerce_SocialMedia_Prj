import { Drawer } from "expo-router/drawer";
import React, { useEffect, useState } from "react";

import { TabBarIcon } from "@/components/navigation/TabBarIcon";
import { Colors } from "@/constants/Colors";
import { useColorScheme } from "@/hooks/useColorScheme";
import { GestureHandlerRootView } from "react-native-gesture-handler";
import { ActivityIndicator, Text, View } from "react-native";
import {
  createDrawerNavigator,
  DrawerContentScrollView,
  DrawerItem,
  DrawerItemList,
} from "@react-navigation/drawer";
import HomeScreen from "./(tabs)/main";
import TabLayout from "./(tabs)/_layout";
import Cart from "./cart";
import Chat from "./chat";
import Order from "./order";
import Post from "./post";
import Search from "./search";
import UserScreen from "./user";
import API, { endpoints } from "@/lib/API";

//  const Drawer = createDrawerNavigator();

const DrawerLayout = () => {
  return (
    <Drawer
      screenOptions={{
        headerShown: true,
        headerTitle: "",
        headerTintColor: "black",
        headerStyle: { backgroundColor: "#ffc13c", height: 35 },
        // headerTransparent: true,
      }}
      // // fetch api categories
      // drawerContent={MyDrawerItem}
    >
      <Drawer.Screen
        name="user"
        options={{
          drawerLabel: "Thông tin người dùng",
        }}
      />
      <Drawer.Screen
        name="(tabs)"
        options={{
          drawerLabel: "Màn hình chính",
        }}
      />

      <Drawer.Screen
        name="cart"
        options={{
          drawerLabel: "Giỏ hàng",
        }}
      />

      <Drawer.Screen
        name="chat"
        options={{
          drawerLabel: "Nhắn tin",
        }}
      />
      <Drawer.Screen
        name="order"
        options={{
          drawerLabel: "Đơn đặt hàng",
        }}
      />
      <Drawer.Screen
        name="post"
        options={{
          drawerLabel: "Bài viết của bạn",
        }}
      />
      <Drawer.Screen
        name="search"
        options={{
          drawerLabel: "Tìm kiếm",
        }}
      />

      <Drawer.Screen
        name="proxyauth"
        options={{
          drawerLabel: "Tài khoản người dùng",
        }}
      />
      {/* <Drawer.Screen
        name="groupbuying"
        options={{
          drawerLabel: "Nhóm mua chung của bạn",
        }}
      /> */}
    </Drawer>
  );
};

export default DrawerLayout;
