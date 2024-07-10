import { useState } from 'react';
import Image from "next/image";
import Link from 'next/link';
import logo from "../assets/logo.svg";
import instagram from "../assets/instagram.svg";


export default function Footer() {
  const [sidebar, setSidebar] = useState(false);

  const handleLinkClick = () => {
    setSidebar(false);
  };

  const openLink = (url) => {
    window.open(url, "_blank");
  };

  return (
    <footer className=" text-white px-14 mb-0 ">
      <div className="container mx-auto flex flex-col md:flex-row items-center justify-between mb-4 pt-10">
        <div className="w-full md:w-1/5 flex flex-col items-left mb-8">
          <Link href="/">
            <Image src={logo} alt="Logo Gitly" width={180} height={180} />
          </Link>
          {/* <p className="text-sm font-text">Vamos Falar sobre Tomada de Decisão Impulsionada por I?</p> */}
        </div>

        <div className="w-full md:w-3/5 mb-4 md:text-center">
          <div className="flex flex-col md:flex-row md:justify-center md:items-center md:space-x-4 items-center">
            <Link href="/" className="mx-2 mb-2 md:mb-0 font-text hover:text-purple-500" onClick={handleLinkClick}>Início</Link>
            <Link href="/ourPurpose" className="mx-2 mb-2 md:mb-0 font-text hover:text-purple-500" onClick={handleLinkClick}>Serviços</Link>
            <Link href="/Partners" className="mx-2 mb-2 md:mb-0 font-text hover:text-purple-500" onClick={handleLinkClick}>Contato</Link>
            <Link href="/Media" className="mx-2 mb-2 md:mb-0 font-text hover:text-purple-500" onClick={handleLinkClick}>Sobre</Link>
            <Link href="/Contact" className="mx-2 mb-2 md:mb-0 font-text hover:text-purple-500" onClick={handleLinkClick}>Planos</Link>
          </div>
        </div>

        <div className="w-full md:w-1/5 flex md:justify-end mb-4 justify-center">
          <button className="mr-4" onClick={() => openLink("https://www.instagram.com/iagosolucoes/")}>
            <Image src={instagram} alt="Instagram" width={30} height={30} />
          </button>
        </div>
      </div>

      <hr className="w-full border-t border-gray-600 mb-4" />

      <div className="text-center mb-4 sm:mb-10">
        <p className="text-xs mb-4 font-text">Copyright © 2024 IAGO | Direitos Reservados</p>
        <p className="text-xs font-text">IAGO - Soluções com inteligência além da artificial.</p>
      </div>
    </footer>
  );
};
