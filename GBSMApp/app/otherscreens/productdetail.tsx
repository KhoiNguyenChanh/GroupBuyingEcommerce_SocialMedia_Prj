// otherscreens/productdetail.jsx
import React, { useEffect, useState } from 'react';
import { View, Text, ActivityIndicator, StyleSheet, Image } from 'react-native';
import API, { endpoints } from "@/lib/API";
import { useRouter } from 'expo-router';

const ProductDetail = () => {
  const route = useRouter();
  const { productId } = route.query;

  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    const loadProduct = async () => {
      try {
        let res = await API.get(`${endpoints["products"]}/${productId}`); 
        console.log("Product detail response:",res.data);
        setProduct(res.data);
      } catch (ex) {
        console.error("Error loading product:", ex);
        setError(true);
      } finally {
        setLoading(false);
      }
    };

    if (productId) {
      loadProduct();
    }
  }, [productId]);

  if (loading) {
    return <ActivityIndicator size="large" color="#000" style={styles.loadingIndicator} />;
  }

  if (error || !product) {
    return <Text style={styles.errorText}>Đã xảy ra lỗi khi tải sản phẩm.</Text>;
  }
  if (!product) {
    return <Text style={styles.noProductsText}>Không tìm thấy sản phẩm.</Text>;
  }

  return (
    <View style={styles.container}>
      <Image source={{ uri: product.image }} style={styles.productImage} resizeMode="cover" />
      <Text style={styles.productName}>{product.name}</Text>
      <Text style={styles.productPrice}>{product.max_price.toLocaleString()} VND</Text>
      <Text style={styles.productDescription}>{product.description}</Text>
      {/* Hiển thị thêm thông tin sản phẩm nếu cần */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#fff",
  },
  productImage: {
    width: '100%',
    height: 300,
    borderRadius: 10,
  },
  productName: {
    fontSize: 24,
    fontWeight: '700',
    marginTop: 20,
    color: "#724c00",
  },
  productPrice: {
    fontSize: 20,
    fontWeight: '500',
    marginTop: 10,
    color: "#724c00",
  },
  productDescription: {
    fontSize: 16,
    marginTop: 10,
    color: "#333",
  },
  loadingIndicator: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  errorText: {
    textAlign: 'center',
    color: 'red',
    fontSize: 16,
    marginTop: 20,
  },
  noProductsText: {
    textAlign: 'center',
    color: "#724c00",
    fontSize: 16,
    marginTop: 20,
  },
});

export default ProductDetail;
