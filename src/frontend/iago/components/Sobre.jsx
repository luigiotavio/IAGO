import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import logo from '../assets/logo.svg';
import sobre from '../assets/sobre.png';

const Sobre = () => {
  return (
    <div className="relative flex flex-col items-center justify-center text-center mt-20 px-20 sm:px-10 h-96 banner-container">
      <Image
        src={sobre}
        alt="Banner"
        layout="fill"
        objectFit="cover"
        quality={100}
        className="banner-image"
      />

      <div className="relative z-10 text-white">
        <h1 className='text-4xl mb-6'>
          Sobre nós
        </h1>
        <p className='mb-10 sm:px-20'>
          Temos como principal objetivo trazer soluções tecnológicas para outras empresas em um
          processo de desenvolvimento mútuo entre cliente e empresa, com a finalidade de desenvolver a melhor solução possível visando um objetivo em comum: o impacto social.
        </p>
        <button className="text-[#7000FF] bg-white hover:shadow-2xl hover:shadow-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto">
          Saiba mais
        </button>
      </div>

      <style jsx>{`
        .banner-container {
          position: relative;
          width: 100%;
          height: 400px; /* Defina a altura desejada para o banner */
          overflow: hidden;
        }
        .banner-image {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
        }
      `}</style>
    </div>
  );
};

export default Sobre;
