import React, {useState, useEffect} from "react"; 
import {getProducts} from "./helper/CoreApiCalls";

export default function Home() {
	const [products, setProducts] = useState([]);
	const [error, setError] = useState(false) 

	const loadAllProducts = () => {
		getProducts()
			.then(data => {
				if (data.error) {
					setError(data.error);
					console.log(error);
					} else {
						setProducts(data); 
					}
			});
	};
	
	useEffect(() => {
		loadAllProducts();
	},); // Silence the eslint-error for missing dependancy. delete [] or implement callback

	return (
		<div>
			<h1>Home Component</h1>
			<div className="row">
				{products.map((product, index) => {
					return(
						<div key={index}>
						<h1>{product.name}</h1>
						</div> 
						);
					}
				)}

			</div>
		</div> 
		);
	}
	
