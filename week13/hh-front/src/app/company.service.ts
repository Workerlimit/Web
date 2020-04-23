import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {HttpClient} from "@angular/common/http';
import {Company} from "./company";
import {LoginResponse} from "./Login";

@Injectable({
  providedIn: 'root'
})

export class CompanyService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http: HttpClient) {}

  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  }

  getCompany(id: number): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/api/companies/${id}/`);
  }

  login(username: string, password: string): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    })
  }
}
