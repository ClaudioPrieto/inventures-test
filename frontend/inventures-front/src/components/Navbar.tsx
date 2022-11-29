import React from "react";
import Icon from "./Icon";

const Navbar = () => {

  return (
    <nav className="w-full shadow-[0_2px_10px_0_rgba(0,0,0,0.5)] h-16 bg-[#0277BD]">
        <div className="flex items-center justify-between pt-2">
          <div className="flex items-center">
            <button className="text-white">
              <Icon type="hamburger-menu"/>
            </button>
            <p className="text-white text-xl">Mi pastillero</p>
          </div>
          <div className="flex items-center">
            <button className="text-white mr-3">
              <Icon type="search"/>
            </button>
            <button className="text-white">
              <Icon type="shopping-cart"/>
            </button>
          </div>
        </div>
    </nav>
  );
}

export default Navbar;
