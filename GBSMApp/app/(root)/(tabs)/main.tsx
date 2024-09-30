import { Image, StyleSheet, Platform,  View, Text, Button, TouchableOpacity } from 'react-native';

import { HelloWave } from '@/components/HelloWave';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useNavigation, useRouter } from "expo-router";
const HomeScreen = () => {
  const route  = useRouter();
  const openDrawer = () => {
    route.push("/(drawer)")
  }
  return (
    <SafeAreaView style={{flex:1, backgroundColor:'#ffc13c'}}>
      
        <Text>IndexView</Text>
        <TouchableOpacity>
          
        </TouchableOpacity>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
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
    position: 'absolute',
  },
});
export default HomeScreen;