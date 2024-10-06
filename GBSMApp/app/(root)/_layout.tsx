import MyContext from '@/lib/MyContext';
import MyUserReducer from '@/lib/MyUserReducer';
import { Stack } from 'expo-router';
import { useContext, useReducer } from 'react';


const Layout = () => {
  const context = useContext(MyContext);
  const [user] = context;
  return (

      <Stack>
        <Stack.Screen name="(drawers)" options={{ headerShown: false }} />
        
      </Stack>
   
  );
}

export default Layout;