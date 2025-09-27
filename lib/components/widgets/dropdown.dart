import 'package:flutter/material.dart'
    show
        BuildContext,
        Container,
        DropdownMenu,
        DropdownMenuEntry,
        State,
        StatefulWidget,
        Widget;

class CreateDropdown<T> extends StatefulWidget {
  final List<DropdownMenuEntry<dynamic>> dropdownMenuEntries;
  final void Function(T?)? onSelected;
  final bool? initiallyVisible;
  final String? placeHolder;

  const CreateDropdown({
    super.key,
    this.initiallyVisible,
    this.placeHolder,
    required this.dropdownMenuEntries,
    required this.onSelected,
  });

  @override
  State<CreateDropdown> createState() => CreateDropdownState();
}

class CreateDropdownState extends State<CreateDropdown> {
  late bool isVisible;

  @override
  void initState() {
    super.initState();
    isVisible = widget.initiallyVisible!;
  }

  void toggleVisibility() {
    setState(() {
      isVisible = !isVisible;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (!isVisible) {
      return Container();
    }

    return DropdownMenu(
      dropdownMenuEntries: widget.dropdownMenuEntries,
      onSelected: widget.onSelected,
      hintText: widget.placeHolder,
    );
  }
}
