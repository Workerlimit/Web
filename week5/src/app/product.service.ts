import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';

import { Product } from './product';
import { Category } from './category';

import { PRODUCTS } from './mock-products';
import { CATEGORIES } from './mock-categories';


@Injectable({ providedIn: 'root' })
export class ProductService {

  constructor() { }

  getProducts(): Observable<Product[]> {
    return of(PRODUCTS);
  }

  getProductsByType(id: number): Observable<Product[]> {
    return of(PRODUCTS.filter(product => product.type === id));
  }

  getProduct(id: number): Observable<Product> {
    return of(PRODUCTS.find(product => product.id === id));
  }

  getCategories(): Observable<Category[]> {
    return of(CATEGORIES);
  }

  getCategory(id: number): Observable<Category> {
    return of(CATEGORIES.find(category => category.id === id));
  }
}
