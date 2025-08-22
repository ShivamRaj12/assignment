// import React, { useEffect, useState } from "react";

// function Products() {
//   const [products, setProducts] = useState([]);

//   useEffect(() => {
//     fetch("/products.json")
//       .then((res) => res.json())
//       .then((data) => setProducts(data));
//   }, []);

//   return (
//     <div className="p-6">
//       <h1 className="text-2xl font-bold mb-4">Scraped Products</h1>
//       <table className="table-auto border-collapse border border-gray-400 w-full">
//         <thead>
//           <tr>
//             <th className="border px-4 py-2">Name</th>
//             <th className="border px-4 py-2">Price</th>
//             <th className="border px-4 py-2">Description</th>
//           </tr>
//         </thead>
//         <tbody>
//           {products.map((p, i) => (
//             <tr key={i}>
//               <td className="border px-4 py-2">{p.name}</td>
//               <td className="border px-4 py-2">{p.price}</td>
//               <td className="border px-4 py-2">{p.description}</td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// }

// export default Products;






