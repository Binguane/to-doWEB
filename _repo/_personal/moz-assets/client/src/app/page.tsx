import Image from "next/image";
import "./page.css";
import SearchBar from "@/components/SearchBar/searchBar";

export default function Home() {
  return (
      <>
      <div className="home__container">
        <div className="home__center-container">
        <h1>MozAssets</h1>
        <SearchBar/>
        </div>
      </div>
      
      </>
  );
}
