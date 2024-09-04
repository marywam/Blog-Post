import React from 'react';
import { Card } from '@shadcn/ui';
import Link from 'next/link';


interface BlogCardProps {
  id: number;
  title: string;
  excerpt: string;
  onDelete: () => void;
}

const BlogCard: React.FC<BlogCardProps> = ({ id, title, excerpt, onDelete }) => {
  return (
    <Card className="my-4">
      <h2 className="text-xl font-bold">{title}</h2>
      <p>{excerpt}</p>
      <div className="mt-4">
        <Link href={`/post/${id}`} className="mr-4">View</Link>
        <button onClick={onDelete} className="text-red-600">Delete</button>
      </div>
    </Card>
  );
};

export default BlogCard;
