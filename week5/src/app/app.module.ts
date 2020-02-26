import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardCategoryComponent } from './dashboard-category/dashboard-category.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { ProductsComponent } from './products/products.component';
import { ProductsByTypeComponent } from './products-by-type/products-by-type.component';

import { SafeUrlPipe } from './shared/safe-url.pipe';



@NgModule({
  declarations: [
    AppComponent,
    DashboardCategoryComponent,
    ProductDetailComponent,
    ProductsComponent,
    ProductsByTypeComponent,
    [SafeUrlPipe]
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
