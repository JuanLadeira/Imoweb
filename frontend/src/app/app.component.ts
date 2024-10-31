import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Felipe';


  transformText() {
    if (isUpperCase(this.title)) {
      this.title = this.title.toLowerCase();
    } else {
      this.title = this.title.toUpperCase();

    }
  }
}
function isUpperCase(text: string): boolean {
  return text === text.toUpperCase();
}
