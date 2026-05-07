import './searchBar.css'
import { Search } from 'lucide-react'

export default function SearchBar(){
    return <div className="search__container">
       <span className='searchBar__logo'>
        <Search/>
        </span> 
        
        <input placeholder='Pesquise Pela Marca' className='search__input' type="text" />
    </div>
}