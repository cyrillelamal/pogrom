# Программирование

![Лабы](./lab.jpg)

```swift
import UIKit

class ViewController: UIViewController, Subscriber {

    @IBOutlet weak var subscriberInfoLabel: UILabel!

    var bloger = Bloger()

    override func viewDidLoad() {
        super.viewDidLoad()
        bloger.subscribe(self)
    }

    @IBAction func publishButton( sender: Any) {
        bloger.releaseVideo()
    }
    @IBAction func subscribeToggle( sender: Any) {
        if (sender as AnyObject).isOn {
            bloger.subscribe(self)
        } else {
            bloger.unsubscribe(self)
        }
    }

    func update(subject: Bloger) {
        subscriberInfoLabel.text = subject.lastVideo
    }
}

//MARK:- Protocols
protocol Subscriber : UIViewController {
    func update(subject : Bloger )
}

//Fix retain cycle
sruct WeakSubscriber { 
    weak var value : Subscriber?
}

class Bloger {

    private lazy var subscribers : [WeakSubscriber] = [] // Массив с подписчиками

    var counter : Int = 0
    var lastVideo = ""

    func subscribe( subscriber: Subscriber) {
        print("subscribed")
        subscribers.append(WeakSubscriber(value: subscriber))
    }

    func unsubscribe( subscriber: Subscriber) {
        subscribers.removeAll(where: { $0.value === subscriber })
        print("unsubscribed")
    }

    func notify() {
        subscribers.forEach { $0.value?.update(subject: self)
        }
    }

    func releaseVideo() {
        counter += 1
        lastVideo = "video" + "(counter)"
        notify()
        print("released!")
    }

}
```
