import {API} from "../../backend";

export const getProducts = () => {
    return fetch(`${API}product`, {method: "GET"}) // fetch products from backend api/product.  
    .then(response => {
	return response.json();
    })
    .catch(err => console.log(err));
};;
