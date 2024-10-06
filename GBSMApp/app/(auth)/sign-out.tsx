import MyContext from "@/lib/MyContext";
import { useContext } from "react";
import { Button, Text } from "react-native";

const Signout = () => {
    // const [user, dispatch] = useContext(MyContext);
    // const logout = () => {
    //     dispatch({
    //         "type": "logout",
            
    //     })
    // }
    return (
        // {user === null ? 
        //     <Button title="login" onPress={logout}/>:
        //     <Button title="logou" onPress={logout}/>
        // }
        <Text>Logout</Text>

        
    )
}
export default Signout;