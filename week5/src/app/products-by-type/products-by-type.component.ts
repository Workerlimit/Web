import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';

import { Product } from '../product';
import { Category } from '../category';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-products-by-type',
  templateUrl: './products-by-type.component.html',
  styleUrls: ['./products-by-type.component.css']
})
export class ProductsByTypeComponent implements OnInit {
  products: Product[];
  typeCategory: Category;

  constructor(
    private productService: ProductService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.getProductsByType();
    this.getCategory();
  }

  getCategory(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getCategory(id)
      .subscribe(category => this.typeCategory = category)
    ;
  }

  getProductsByType(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProductsByType(id)
      .subscribe(products => this.products = products)
    ;
  }
}
