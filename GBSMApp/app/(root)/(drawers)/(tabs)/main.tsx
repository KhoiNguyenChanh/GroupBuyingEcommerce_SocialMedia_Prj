import {
  Image,
  StyleSheet,
  View,
  Text,
  TouchableOpacity,
  ActivityIndicator,
  ScrollView,
} from "react-native";

import { SafeAreaView } from "react-native-safe-area-context";
import { useNavigation, useRouter } from "expo-router";
import React, { useEffect, useState } from "react";
import API, { endpoints } from "@/lib/API";

const HomeScreen = () => {
  const route = useRouter();

  const [prods, setProds] = useState(null);
  React.useEffect(() => {
    const loadProducts = async () => {
      try {
        // console.log("Gửi yêu cầu đến API...");
        let res = await API.get(endpoints["products"]);
        // res.data là dữ liệu đổ ra có thể xem dc trên swagger
        // console.log("Phản hồi từ API:", res.data);
        setProds(res.data); //setProds(res.data.results)
      } catch (ex) {
        console.error("Error loading products:", ex);
      }
    };
    loadProducts();
  }, []);

  return (
    <SafeAreaView
      style={{
        flex: 1,
        backgroundColor: "#ffc13c",
        justifyContent: "center",
        // alignItems: "center",
        //rember this one below
        bottom:15,
      }}
    >
      <Text>IndexView</Text>
      <ScrollView
        style={{ flex:1,   backgroundColor: "red" }}
      >
        {prods === null ? (
          <ActivityIndicator />
        ) : (
          <>
            {prods.map((p) => (
              <View
                key={p.id}
                style={{ flex:1, margin: 5, flexDirection: "row" }}
              >
                  <TouchableOpacity>
                    <Image
                    source={{
                      uri: p.image,
                    }}
                    style={{ width: 100, height: 100 }}
                    resizeMode="contain"
                  />
                  </TouchableOpacity>
                  
                  <TouchableOpacity>
                    <Text>{p.name}</Text>
                  </TouchableOpacity>
                  {/* <Text>{p.description}</Text> */}
              </View>
            ))}
          </>
        )}
       
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: "row",
    alignItems: "center",
    gap: 8,
  },
  scrollviewcontainer: {
    //ben trai co tieu de
    //ben phai co gi
    flex: 1,
    flexDirection: "row",
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: "absolute",
  },
});
export default HomeScreen;
