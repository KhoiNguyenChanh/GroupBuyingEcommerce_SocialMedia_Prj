import { Stack } from 'expo-router';

const ScreenLayout = () => {
  return (
      <Stack screenOptions={{headerShown:false,}}>
        <Stack.Screen name="checkout"/>
        <Stack.Screen name="productdetail"/>
        <Stack.Screen name="productform"/>
        <Stack.Screen name="shopform"/>
        <Stack.Screen name="shop"/>
        <Stack.Screen name="userinfoedit"/>

      </Stack>
   
  );
}

export default ScreenLayout;