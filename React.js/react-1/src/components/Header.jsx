import reactlogo from "/src/assets/react.svg"

export default function Header(){
                   return(
                       <header className="header">
                           <img src={reactlogo}  className="react-logo" alt="react logo" />
                           <nav className="nav-bar">
                               <ul className="nav-list">
                                   <li className="list-item">Pricing</li>
                                   <li className="list-item">About</li>
                                   <li className="list-item">Contact</li>
                               </ul>
                           </nav>
                       </header>
                          )
                   }