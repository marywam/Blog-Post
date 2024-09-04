// src/components/Header.tsx

import * as React from "react";
import Link  from "next/link"; // Use Next.js Link component

const Header: React.FC = () => {
  return (
    <header className="p-4 bg-gray-800 text-white">
      <nav className="flex justify-between container mx-auto">
        <Link href="/" className="text-xl font-bold">
          Blog Platform
        </Link>
        <Link href="/posts/create" className="text-sm">
          Create New Post
        </Link>
      </nav>
    </header>
  );
}

export default Header;
