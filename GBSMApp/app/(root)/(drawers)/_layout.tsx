import { Drawer } from "expo-router/drawer";
import React, { useContext, useEffect, useState } from "react";
import MyContext from "@/lib/MyContext";

//  const Drawer = createDrawerNavigator();

const DrawerLayout = () => {
  const [user] = useContext(MyContext);
  useEffect(() => {
    console.log("User updated:", user);
  }, [user]);
  // co xuat ten user admin, nhung khong thay doi dc :1
  return (
    <Drawer
      screenOptions={{
        headerShown: true,
        headerTitle: "",
        headerTintColor: "black",
        headerStyle: { backgroundColor: "#ffc13c", height: 35 },
      }}
    >
      <Drawer.Screen
        name="proxyauth"
        options={{
          drawerLabel: user ? user.username : "Tài khoản người dùng",
        }}
      />
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
