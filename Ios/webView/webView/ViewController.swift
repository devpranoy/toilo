//
//  ViewController.swift
//  webView
//
//  Created by Rohan Tony on 28/02/18.
//  Copyright © 2018 trohan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var webView: UIWebView!
    override func viewDidLoad(){
        super.viewDidLoad()
    let url = URL(string:"https://www.apple.com")
    let urlRequest = URLRequest(url: url!)
    webView.loadRequest(urlRequest)
 }
}

