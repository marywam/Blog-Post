import React from 'react';
import Link from 'next/link';

const Header = () => {
  return (
    <header className="bg-gray-800 p-4 text-white">
      <nav className="flex justify-between">
        <h1 className="text-xl">Simple Blog</h1>
        <div>
          <Link href="/">Home</Link>
          <Link href="/create" className="ml-4">Create Post</Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;
