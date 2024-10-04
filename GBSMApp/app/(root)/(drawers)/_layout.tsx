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
      <Drawer.Screen name="user" />
      <Drawer.Screen
        name="proxyauth"
        options={{
          drawerLabel: "Tài khoản người dùng",
        }}
      />
    </Drawer>
  );
};

export default DrawerLayout;

// const MyDrawerItem = (props) => {
//   const [categories, setCategories] = useState([]);
//   useEffect(() => {
//     const loadCategories = async () => {
//       try {
//         let res = await API.get(endpoints["categories"]);
//         console.log("danh sach cate:", res.data);
//         setCategories(res.data);
//       } catch (ex) {
//         setCategories([]);
//         console.error(ex);
//       }
//       loadCategories();
//     };
//   }, []);
//   return (
//     // draweritemlist la danh sach nhung screen nap o trong cai navigation
//     //
//     <DrawerContentScrollView {...props}>
//       <DrawerItemList {...props} />
//       {categories === null ? (
//         <ActivityIndicator />
//       ) : (
//         <>
//           {categories.map((c) => (
//             <DrawerItem
//               key={c.id}
//               label={c.name}
//               onPress={() =>
//                 props.navigation.navigate("cart", { cateId: c.id })
//               }
//             />
//           ))}
//         </>
//       )}
//     </DrawerContentScrollView>
//   );
// };



// const MyDrawerItem = (props)=>{
//   return(
//     <DrawerContentScrollView{...props}>
//     // draweritemlist la danh sach nhung screen nap o trong cai navigation
//       <DrawerItemList></DrawerItemList>
//     </DrawerContentScrollView>
//   )
// }

// <Drawer.Navigator >
//     <Drawer.Screen name="main" component={TabLayout} />
//     <Drawer.Screen name="social" component={TabLayout} />

//     <Drawer.Screen name="cart" component={Cart}/>
//     <Drawer.Screen name="chat" component={Chat}/>
//     <Drawer.Screen name="order" component={Order}/>
//     <Drawer.Screen name="post" component={Post}/>
//     <Drawer.Screen name="search" component={Search}/>
//     <Drawer.Screen name="user" component={UserScreen}/>
// </Drawer.Navigator>
// <GestureHandlerRootView>
// </GestureHandlerRootView>

// <Drawer>
// <Drawer.Screen name="TabNavigator" options={{ headerShown: false }} />
//   <Drawer.Screen
//       name="funny" // This is the name of the page and must match the url from root
//       options={{
//         drawerLabel: 'Home',
//         title: 'overview',
//       }}
//     />
//     <Drawer.Screen
//       name="user" // This is the name of the page and must match the url from root
//       options={{
//         drawerLabel: 'User',
//         title: 'overview',
//       }}
//     />
// </Drawer>
