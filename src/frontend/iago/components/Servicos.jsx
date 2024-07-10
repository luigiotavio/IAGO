import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import logo from '../assets/logo.svg';

const Servicos = () => {

  return (
    <div>

      <div className="flex flex-wrap mt-10">
        <div class="flex-1 bg-[#7000FF17] p-4 sm:mr-4 mr-0 mb-4 text-center ">
          <h2 className='text-xl'>
            Marketing digital
          </h2>
          <p className='px-14 mt-4 text-[#FFFFFF43]'>
          Lorem Ipsum is simply dummy text of the printing and typesetting industry.
          </p>
        </div>
        <div class="flex-1 bg-[#7000FF17] p-4 mb-4 text-center ">
          <h2 className='text-xl'>
            Marketing digital
          </h2>
          <p className='px-14 mt-4 text-[#FFFFFF43]'>
          Lorem Ipsum is simply dummy text of the printing and typesetting industry.
          </p>
        </div>
        <div class="flex-1 bg-[#7000FF17] p-4 sm:ml-4 ml-0 mb-4 text-center ">
          <h2 className='text-xl'>
            Marketing digital
          </h2>
          <p className='px-14 mt-4 text-[#FFFFFF43]'>
          Lorem Ipsum is simply dummy text of the printing and typesetting industry.
          </p>
        </div>

    </div>
    </div>

  );
};

export default Servicos;
