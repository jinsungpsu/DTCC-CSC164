# ListView and Observable Lists

---

# Overview

- Display typed items in a ListView
- Add, remove, clear, and select items
- Connect an ObservableList to a ListView

---

# ListView Class

---

# ListView
- Similar to an ArrayList for viewing data.
- Uses generic type parameters.

```java
ListView<String> myListView = new ListView<>();
```

<!-- footer -->
https://jenkov.com/tutorials/javafx/listview.html

---

# Adding Items

```java
myListView.getItems().add("hello");
```

<!-- footer -->
https://jenkov.com/tutorials/javafx/listview.html

---

# Removing Items
- Remove by index

```java
myListView.getItems().remove(1);
```

- Remove by range

```java
myListView.getItems().remove(0,2);
```

- Remove by object

```java
myListView.getItems().remove(...);
```

- Clear all

```java
myListView.getItems().clear();
```

---

# ListView Selected Item

```java
String selectedString = myListView.getSelectionModel().getSelectedItem();
```

<!-- footer -->
https://jenkov.com/tutorials/javafx/listview.html

---

# Changing ListView Contents
- Think of ListView as a place to view data.
- View, clear, change, and reload items as needed.

---

# Using an ObservableList

```java
ArrayList<String> itemList = new ArrayList<>();
ObservableList<String> observableItems = FXCollections.observableArrayList(itemList);
ListView<String> listView = new ListView<>();
listView.setItems(observableItems);
```

---

# What is an Observable List?
- It is a class.
- Automatically notifies the UI when contents change.
- ArrayList does not automatically notify the UI.
- ObservableList keeps UI and data synchronized.

---

# Manually Viewing

```java
for (String item : itemList) {
    listView.getItems().add(item);
}
```

---

# Clearing, Refreshing

```java
listView.getItems().clear();
listView.getItems().refresh();
```

---

# Summary

- ListView displays items and exposes a selection model
- Use getItems() to access and change displayed items
- An ObservableList notifies listeners when its contents change
- Update the list connected to the view to keep displayed data synchronized
