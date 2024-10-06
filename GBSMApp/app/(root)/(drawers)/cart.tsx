import { Redirect, useNavigation, useRouter } from "expo-router";
import { useState } from "react";
import {
   
  StyleSheet,
  Text,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

const Cart = () => {
  const [products, setProducts] = useState([
    {
      id: 1,
      name: 'Apple iPhone 15 (128 GB) - Black',
      description:
          'INNOVATIVE DESIGN, 48MP CAMERA, LE FUNNY',
      price: '900',
      quantity: 1,
      category: 'mobile',
      image: 'https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-den-1.jpg'


  },
  {
      id: 3,
      name: 'Apple iPhone 15 (128 GB) - Gold',
      description:
          'INNOVATIVE DESIGN, 48MP CAMERA, LE FUNNY',
      price: '300',
      quantity: 1,
      category: 'mobile',
      image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ19YxbSz4rdLfPzqGsujlKwGybhP0LFT0zSIzLrTR7UQ&s'

  },
  {
      id: 4,
      name:'Apple iPhone 15 (128 GB) - Green',
      description:
      'INNOVATIVE DESIGN, 48MP CAMERA, LE FUNNY',
      price:'100',
      quantity: 1,
      category:'mobile',
      image:'https://brotherselectronicsbd.com/image/cache/catalog/demo/product/Apple/iphone%2015/iphon-15-(1)-9691-800x800.jpg'

  },
  
]);
const navigation = useNavigation();
const route = useRouter();

   return (
    <SafeAreaView>
        <Text>
            Cart
        </Text>
    </SafeAreaView>
   )
};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
export default Cart;
