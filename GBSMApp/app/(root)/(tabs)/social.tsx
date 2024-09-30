import { Colors } from '@/constants/Colors';
import Ionicons from '@expo/vector-icons/Ionicons';
import { StyleSheet, Image, Platform,  View, Text } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';


const SocialMediaScreen = () => {
    return (
      <SafeAreaView>
          <Text>SocialMediaScreen</Text>
      </SafeAreaView>
    );
}
export default SocialMediaScreen;


const styles = StyleSheet.create({
  headerImage: {
    color: '#808080',
    bottom: -90,
    left: -35,
    position: 'absolute',
  },
  titleContainer: {
    flexDirection: 'row',
    gap: 8,
  },
});
