// import {
//   Image,
//   StyleSheet,
//   View,
//   Text,
//   TouchableOpacity,
//   ActivityIndicator,
//   ScrollView,
//   Dimensions,
//   ImageBackground,
// } from "react-native";

// import { SafeAreaView } from "react-native-safe-area-context";
// import { useNavigation, useRouter } from "expo-router";
// import React, { useEffect, useState } from "react";
// import API, { endpoints } from "@/lib/API";
// import SwiperFlatList from "react-native-swiper-flatlist";

// const bannerImage = require("@/assets/images/banner/banner4.jpg");

// const HomeScreen = () => {
//   function renderBanner() {
//     return (
//       <View style={styles.bannerContainer}>
//         <ImageBackground
//           source={bannerImage}
//           style={styles.bannerImage}
//           resizeMode="cover"
//         />
//         <Text style={styles.bannerText}>WELCOME TO OUR APP!</Text>
//       </View>
//     );
//   }
//   const textColor = "#724c00";
//   const route = useRouter();
//   const handleProduct = () => {
//     route.push("/otherscreensproductdetail");
//   };

//   const [prods, setProds] = useState([]);
//   const [categories, setCategories] = useState([]);
//   const [selectedCategory, setSelectedCategory] = useState(null); // Lưu trữ danh mục được chọn
//   const [filteredProducts, setFilteredProducts] = useState(prods); // Lưu trữ danh sách sản phẩm đã lọc
//   const [loadingProds, setLoadingProds] = useState(true); // Trạng thái tải sản phẩm
//   const [loadingCategories, setLoadingCategories] = useState(true); // Trạng thái tải danh mục

//   React.useEffect(() => {
//     // load categories
//     const loadCategories = async () => {
//       try {
//         let res = await API.get(endpoints["categories"]);
//         // console.log("Categories response:", res.data);
//         setCategories(res.data);
//       } catch (ex) {
//         console.error("Error loading categories:", ex);
//       } finally {
//         setLoadingCategories(false);
//       }
//     };
//     // load products
//     const loadProducts = async () => {
//       try {
//         // console.log("Gửi yêu cầu đến API...");
//         let res = await API.get(endpoints["products"]);
//         // console.log("Phản hồi từ API:", res.data);
//         setProds(res.data); //setProds(res.data.results)
//         setFilteredProducts(res.data);
//       } catch (ex) {
//         console.error("Error loading products:", ex);
//       } finally {
//         setLoadingProds(false);
//       }
//     };

//     loadCategories();
//     loadProducts();
//   }, []);

//   const handleCategories = (categoryId) => {
//     if (categoryId === selectedCategory) {
//       setSelectedCategory(null);
//       setFilteredProducts(prods);
//     } else {
//       setSelectedCategory(categoryId);
//       const filtered = prods.filter(
//         (product) => product.categoryId === categoryId
//       );
//       setFilteredProducts(filtered);
//     }
//   };
//   return (
//     <SafeAreaView style={styles.container}>
//       <ScrollView>
//         {renderBanner()}
//         {/* categories */}
//         <View style={{ flex: 1, backgroundColor: "#ffd16f" }}>
//           <Text style={styles.categoryTitle}>Danh mục sản phẩm</Text>

//           <ScrollView horizontal showsHorizontalScrollIndicator={false}>
//             {loadingCategories ? (
//               <ActivityIndicator />
//             ) : (
//               <>
//                 {/* category all prods */}
//                 <View
//                   style={{ margin: 6, padding: 5, justifyContent: "center" }}
//                 >
//                   <TouchableOpacity
//                     style={[
//                       { borderRadius: 10, backgroundColor: "#ffd889" },
//                       selectedCategory === null &&
//                         styles.selectedCategoryButton,
//                     ]}
//                     onPress={() => handleCategories(null)}
//                   >
//                     <Text
//                       style={[
//                         {
//                           fontWeight: "700",
//                           fontSize: 15,
//                           padding: 10,
//                           color: textColor,
//                         },
//                         selectedCategory === null && { color: "white" },
//                       ]}
//                     >
//                       Tất cả
//                     </Text>
//                   </TouchableOpacity>
//                 </View>
//                 {/* san pham theo danh muc */}
//                 {categories.map((c) => (
//                   <View
//                     key={c.id}
//                     style={{ margin: 6, padding: 5, justifyContent: "center" }}
//                   >
//                     <TouchableOpacity
//                       style={[
//                         { borderRadius: 10, backgroundColor: "#ffd889" },
//                         selectedCategory === c.id &&
//                           styles.selectedCategoryButton,
//                       ]}
//                       onPress={() => handleCategories(c.id)}
//                     >
//                       <Text
//                         style={[
//                           {
//                             fontWeight: "700",
//                             fontSize: 15,
//                             padding: 10,
//                             color: textColor,
//                           },
//                           selectedCategory === c.id && { color: "white" },
//                         ]}
//                       >
//                         {c.name}
//                       </Text>
//                     </TouchableOpacity>
//                   </View>
//                 ))}
//               </>
//             )}
//           </ScrollView>
//         </View>
//         {/* scrollview2 for product */}
//         <View style={{ flex: 4 }}>
//           <Text
//             style={{
//               color: textColor,
//               marginHorizontal: 10,
//               marginTop: 5,
//               fontSize: 17,
//               fontWeight: "500",
//             }}
//           >
//             Sản phẩm hôm nay
//           </Text>

//           <ScrollView style={styles.scrollView}>
//             {loadingProds ? (
//               <ActivityIndicator />
//             ) : filteredProducts.length === 0 ? (
//               <Text style={styles.noProductsText}>Không có sản phẩm nào.</Text>
//             ) : (
//               <View style={styles.gridContainer}>
//                 {filteredProducts.map((p) => (
//                   <View key={p.id} style={styles.productCard}>
//                     <TouchableOpacity
//                       onPress={() => {
//                         route.push("/otherscreens/productdetail");
//                       }}
//                     >
//                       <Image
//                         source={{
//                           uri: p.image,
//                         }}
//                         style={styles.productImage}
//                         resizeMode="cover"
//                       />
//                     </TouchableOpacity>

//                     <TouchableOpacity style={{ margin: 10 }}>
//                       <Text
//                         style={[
//                           { color: textColor, fontSize: 15, fontWeight: "700" },
//                         ]}
//                         numberOfLines={1}
//                         ellipsizeMode="tail"
//                       >
//                         {p.name}
//                       </Text>
//                       <Text style={{ color: textColor }}>
//                         {p.max_price.toLocaleString()} VND
//                       </Text>
//                     </TouchableOpacity>

//                     {/* <Text>{p.description}</Text> */}
//                   </View>
//                 ))}
//               </View>
//             )}
//           </ScrollView>
//         </View>
//       </ScrollView>
//     </SafeAreaView>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#ffc13c",
//     // bottom: 30,
//   },
//   selectedCategoryButton: {
//     backgroundColor: "#ffa500", // Màu khi danh mục được chọn
//   },
//   categoryTitle: {
//     marginHorizontal: 10,
//     top: 5,
//     fontSize: 15,
//     fontWeight: "500",
//     color: "#724c00",
//   },
//   scrollView: {
//     // flex: 2,
//     // backgroundColor: "red",
//   },
//   productContainer: {
//     flex: 1,
//     margin: 5,
//     flexDirection: "row",
//   },
//   gridContainer: {
//     flexDirection: "row",
//     flexWrap: "wrap", // Cho phép các sản phẩm chia thành nhiều hàng
//     justifyContent: "space-evenly", // Tạo khoảng cách đều giữa các cột
//     alignItems: "center",
//     marginHorizontal: 5,
//   },
//   productImage: {
//     width: "100%",
//     height: 150,
//     borderTopRightRadius: 10,
//     borderTopLeftRadius: 10,
//   },
//   productTitle: {
//     fontSize: 18,
//     fontWeight: "bold",
//     marginBottom: 8,
//   },
//   productCard: {
//     width: "48%", // Mỗi card chiếm 48% chiều rộng để có khoảng cách giữa chúng
//     marginBottom: 15, // Khoảng cách giữa các dòng
//     // borderWidth: 1,
//     backgroundColor: "#ffd889",
//     borderRadius: 10,
//   },

//   productName: {
//     marginTop: 5,
//     textAlign: "center",
//   },
//   bannerContainer: {
//     alignItems: "center",
//     // marginBottom: 16,
//   },
//   bannerImage: {
//     width: "100%", // Chiếm hết chiều rộng
//     height: 200, // Chiều cao banner
//   },
//   bannerText: {
//     position: "absolute", // Để hiển thị trên ảnh
//     color: "#fff",
//     fontSize: 24,
//     fontWeight: "bold",
//   },
//   categoryContainer: {
//     padding: 16,
//   },
//   noProductsText: {
//     textAlign: "center",
//     color: "#724c00",
//     fontSize: 16,
//     marginTop: 20,
//   },
//   categoryTitle: {
//     fontSize: 18,
//     fontWeight: "bold",
//     marginBottom: 8,
//   },
//   categoryCard: {
//     marginRight: 10,
//     width: 100,
//     alignItems: "center",
//   },
//   categoryImage: {
//     width: 100,
//     height: 100,
//     borderRadius: 10,
//   },
//   categoryName: {
//     marginTop: 5,
//     textAlign: "center",
//   },
// });

// export default HomeScreen;
import React, { useState, useEffect } from 'react';
import { 
  SafeAreaView, 
  View, 
  Text, 
  ScrollView, 
  TouchableOpacity, 
  Image, 
  ImageBackground, 
  ActivityIndicator, 
  StyleSheet 
} from 'react-native';
import { useRouter } from 'expo-router'; // Hoặc thư viện routing bạn đang sử dụng
import API, { endpoints } from '@/lib/API'; // Đảm bảo bạn đã cấu hình API đúng cách
import { useNavigation } from '@react-navigation/native';

const bannerImage = require("@/assets/images/banner/banner4.jpg");

const HomeScreen = () => {
  const [prods, setProds] = useState([]); // Tất cả sản phẩm
  const [categories, setCategories] = useState([]); // Danh mục sản phẩm
  const [selectedCategory, setSelectedCategory] = useState(null); // Danh mục đang chọn
  const [filteredProducts, setFilteredProducts] = useState([]); // Sản phẩm sau khi lọc
  const [loadingProds, setLoadingProds] = useState(true); // Trạng thái tải sản phẩm
  const [loadingCategories, setLoadingCategories] = useState(true); // Trạng thái tải danh mục

  const textColor = "#724c00";
  const route = useRouter();
  const navigation = useNavigation();
  useEffect(() => {
    // Tải danh mục
    const loadCategories = async () => {
      try {
        let res = await API.get(endpoints["categories"]);
        setCategories(res.data);
      } catch (ex) {
        console.error("Error loading categories:", ex);
      } finally {
        setLoadingCategories(false);
      }
    };

    // Tải sản phẩm
    const loadProducts = async () => {
      try {
        let res = await API.get(endpoints["products"]);
        setProds(res.data);
        setFilteredProducts(res.data); // Ban đầu hiển thị tất cả sản phẩm
      } catch (ex) {
        console.error("Error loading products:", ex);
      } finally {
        setLoadingProds(false);
      }
    };

    loadCategories();
    loadProducts();
  }, []);

  // Cập nhật filteredProducts khi prods hoặc selectedCategory thay đổi
  useEffect(() => {
    if (selectedCategory === null) {
      setFilteredProducts(prods);
    } else {
      const filtered = prods.filter((product) => {
        // Kiểm tra xem thuộc tính categoryId có tồn tại hay không
        // Thay 'categoryId' bằng tên thuộc tính đúng nếu cần
        return product.category === selectedCategory;
      });
      setFilteredProducts(filtered);
      console.log(filtered);
    }
  }, [prods, selectedCategory]);

  // Hàm xử lý khi nhấn vào danh mục
  const handleCategoryPress = (category) => {
    if (category === selectedCategory) {
      // Nếu đã chọn danh mục này, bỏ chọn để hiển thị tất cả sản phẩm
      setSelectedCategory(null);
    } else {
      setSelectedCategory(category);
    }
  };

  // Hàm hiển thị banner
  const renderBanner = () => (
    <View style={styles.bannerContainer}>
      <ImageBackground
        source={bannerImage}
        style={styles.bannerImage}
        resizeMode="cover"
      >
        <Text style={styles.bannerText}>WELCOME TO OUR APP!</Text>
      </ImageBackground>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView>
        {/* Banner */}
        {renderBanner()}

        {/* Danh mục sản phẩm */}
        <View style={styles.categoryContainer}>
          <Text style={styles.categoryTitle}>Danh mục sản phẩm</Text>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.categoryScroll}>
            {loadingCategories ? (
              <ActivityIndicator size="small" color="#000" />
            ) : (
              <>
                {/* Tùy chọn "Tất cả" */}
                <View style={styles.categoryItem}>
                  <TouchableOpacity
                    style={[
                      styles.categoryButton,
                      selectedCategory === null && styles.selectedCategoryButton,
                    ]}
                    onPress={() => handleCategoryPress(null)}
                  >
                    <Text style={[
                      styles.categoryText,
                      selectedCategory === null && styles.selectedCategoryText,
                    ]}>
                      Tất cả
                    </Text>
                  </TouchableOpacity>
                </View>

                {/* Các danh mục từ API */}
                {categories.map((c) => (
                  <View key={c.id} style={styles.categoryItem}>
                    <TouchableOpacity
                      style={[
                        styles.categoryButton,
                        selectedCategory === c.id && styles.selectedCategoryButton,
                      ]}
                      onPress={() => handleCategoryPress(c.id)}
                    >
                      <Text style={[
                        styles.categoryText,
                        selectedCategory === c.id && styles.selectedCategoryText,
                      ]}>
                        {c.name}
                      </Text>
                    </TouchableOpacity>
                  </View>
                ))}
              </>
            )}
          </ScrollView>
        </View>

        {/* Sản phẩm */}
        <View style={styles.productSection}>
          <Text style={styles.productSectionTitle}>Sản phẩm hôm nay</Text>
          {loadingProds ? (
            <ActivityIndicator size="large" color="#000" style={styles.loadingIndicator} />
          ) : (
            filteredProducts.length === 0 ? (
              <Text style={styles.noProductsText}>Không có sản phẩm nào.</Text>
            ) : (
              <View style={styles.gridContainer}>
                {filteredProducts.map((p) => (
                  <View key={p.id} style={styles.productCard}>
                    <TouchableOpacity
                      onPress={() => {
                        // navigation.navigate( route.push("/otherscreens/productdetail/"), {productId: p.id})
                        route.push(`/otherscreens/productdetail?productId=${p.id}`);
                      }}
                    >
                      <Image
                        source={{ uri: p.image }}
                        style={styles.productImage}
                        resizeMode="cover"
                      />
                    </TouchableOpacity>

                    <View style={styles.productInfo}>
                      <Text style={styles.productName} numberOfLines={1} ellipsizeMode="tail">
                        {p.name}
                      </Text>
                      <Text style={styles.productPrice}>
                        {p.max_price.toLocaleString()} VND
                      </Text>
                    </View>
                  </View>
                ))}
              </View>
            )
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

// StyleSheet được cập nhật để hỗ trợ các thay đổi
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#ffd16f",
  },
  bannerContainer: {
    width: '100%',
    height: 200,
    position: 'relative',
  },
  bannerImage: {
    width: '100%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  bannerText: {
    color: '#fff',
    fontSize: 24,
    fontWeight: '700',
    backgroundColor: 'rgba(0,0,0,0.5)',
    padding: 10,
    borderRadius: 5,
  },
  categoryContainer: {
    backgroundColor: "#ffd16f",
    paddingVertical: 10,
  },
  categoryTitle: {
    marginHorizontal: 10,
    fontSize: 15,
    fontWeight: "500",
    color: "#724c00",
    marginBottom: 10,
  },
  categoryScroll: {
    paddingHorizontal: 10,
  },
  categoryItem: {
    marginRight: 10,
  },
  categoryButton: {
    borderRadius: 10,
    backgroundColor: "#ffd889",
    paddingVertical: 10,
    paddingHorizontal: 15,
  },
  selectedCategoryButton: {
    backgroundColor: "#ffa500", // Màu khi danh mục được chọn
  },
  categoryText: {
    fontWeight: "700",
    fontSize: 15,
    color: "#724c00",
  },
  selectedCategoryText: {
    color: "#fff", // Màu chữ khi danh mục được chọn
  },
  productSection: {
    flex: 4,
    paddingHorizontal: 10,
    paddingTop: 10,
  },
  productSectionTitle: {
    color: "#724c00",
    marginBottom: 10,
    fontSize: 17,
    fontWeight: '500',
  },
  scrollView: {
    flex: 1,
  },
  gridContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  productCard: {
    width: '48%',
    backgroundColor: '#fff',
    borderRadius: 10,
    overflow: 'hidden',
    marginBottom: 15,
    // Shadow cho iOS
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    // Elevation cho Android
    elevation: 2,
  },
  productImage: {
    width: '100%',
    height: 150,
  },
  productInfo: {
    padding: 10,
  },
  productName: {
    color: "#724c00",
    fontSize: 15,
    fontWeight: '700',
  },
  productPrice: {
    color: "#724c00",
    fontSize: 14,
    fontWeight: '500',
    marginTop: 5,
  },
  loadingIndicator: {
    marginTop: 20,
  },
  noProductsText: {
    textAlign: 'center',
    color: "#724c00",
    fontSize: 16,
    marginTop: 20,
  },
});

export default HomeScreen;
