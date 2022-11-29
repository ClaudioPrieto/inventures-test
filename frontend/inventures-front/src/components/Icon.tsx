export interface IconProps {
    iconType: string
}

const Icon = ({iconType}: IconProps) => {
  switch(iconType) {
    case 'burger-menu':
      return <img src='burger-menu.svg' alt="burger-menu"/>
    case 'shopping-cart':
      return <img src='shopping-cart.svg' alt="shopping-cart" className="p-3"/>
    case 'search':
        return <img src='search.svg' alt="search" className=""/>
    case 'black-shopping-cart':
      return (
      <div className="relative">
        <img src='black-shopping-cart.svg' alt="black-shopping-cart" className="p-3"/>
        <img src='add-circle.svg' alt="add-circle" className="absolute top-3 right-3"/>
      </div>
      )
    default:
      return null
  }
}

export default Icon;
