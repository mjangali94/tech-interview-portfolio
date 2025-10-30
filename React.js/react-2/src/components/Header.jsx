import globe from "/src/assets/globe.png"

export default function Header(){
                   return(
                       <header className="header">
                           <img src={globe}  className="react-logo" alt="globe icon" />
                           <h1>my travel journal!</h1>
                       </header>
                          )
                   }